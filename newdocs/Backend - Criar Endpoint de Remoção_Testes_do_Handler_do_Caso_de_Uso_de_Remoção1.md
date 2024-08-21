```csharp
namespace Project.Tests.Application.UseCases.Brands
{
    public class DeleteBrandHandlerTest
    {
        private readonly IBrandRepository _brandRepository = Substitute.For<IBrandRepository>();
        private readonly IUnitOfWork _unitOfWork = Substitute.For<IUnitOfWork>();
        private readonly DeleteBrandHandler _handler;

        public DeleteBrandHandlerTest()
        {
            _handler = new DeleteBrandHandler(_brandRepository, _unitOfWork);
        }

        [Fact]
        public async Task Handle_DeletesBrand()
        {
            // Arrange
            var command = BrandHelper.RandomDeleteBrandCommand();
            var brand = EntityFaker.RandomBrand();

            _brandRepository.GetByIdAsync(command.Id).Returns(brand);

            // Act
            await _handler.Handle(command, CancellationToken.None);

            // Assert
            _brandRepository.Received(1).Delete(brand);
            await _unitOfWork.Received(1).CommitAsync(CancellationToken.None);
        }

        [Fact]
        public async Task Handle_ThrowsNotFoundException_WhenBrandNotFound()
        {
            // Arrange
            var command = BrandHelper.RandomDeleteBrandCommand();

            _brandRepository.GetByIdAsync(command.Id).Returns((Brand)null);

            // Act & Assert
            var exception = await Assert.ThrowsAsync<NotFoundException>(() => _handler.Handle(command, CancellationToken.None));
            Assert.Equal("Brand not found", exception.Message);
        }
    }
}
```