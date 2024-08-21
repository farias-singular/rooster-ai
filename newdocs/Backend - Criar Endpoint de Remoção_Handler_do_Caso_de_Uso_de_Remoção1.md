```csharp
namespace Project.Application.UseCases.Brands.DeleteBrand
{
    public class DeleteBrandHandler : ICommandHandler<DeleteBrandCommand>
    {
        private readonly IBrandRepository _brandRepository;
        private readonly IUnitOfWork _unitOfWork;

        public DeleteBrandHandler(
            IBrandRepository brandRepository,
            IUnitOfWork unitOfWork)
        {
            _brandRepository = brandRepository;
            _unitOfWork = unitOfWork;
        }

        public async Task<Unit> Handle(DeleteBrandCommand command, CancellationToken ct = default)
        {
            var brand = await _brandRepository.GetByIdAsync(command.Id);
            if (brand == null)
            {
                throw new NotFoundException("Brand not found");
            }

            _brandRepository.Delete(brand);
            await _unitOfWork.CommitAsync(ct);

            return Unit.Value;
        }
    }
}
```