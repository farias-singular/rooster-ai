```csharp
namespace Project.Application.UseCases.Brands.UpdateBrand
{
    public class UpdateBrandHandler : ICommandHandler<UpdateBrandCommand, UpdateBrandDto>
    {
        private readonly IBrandRepository _brandRepository;
        private readonly IOrganizationRepository _organizationRepository;
        private readonly ICategoryRepository _categoryRepository;
        private readonly IUnitOfWork _unitOfWork;
        private readonly IMapper _mapper;

        public UpdateBrandHandler(
            IBrandRepository brandRepository,
            IOrganizationRepository organizationRepository,
            ICategoryRepository categoryRepository,
            IUnitOfWork unitOfWork,
            IMapper mapper)
        {
            _brandRepository = brandRepository;
            _organizationRepository = organizationRepository;
            _categoryRepository = categoryRepository;
            _unitOfWork = unitOfWork;
            _mapper = mapper;
        }

        public async Task<UpdateBrandDto> Handle(UpdateBrandCommand command, CancellationToken ct = default)
        {
            var brand = await _brandRepository.GetByIdAsync(command.Id);
            if (brand == null)
            {
                throw new NotFoundException("Brand not found");
            }

            var organization = await _organizationRepository.GetByIdAsync(command.OrganizationId);
            if (organization == null)
            {
                throw new NotFoundException("Organization not found");
            }

            var category = await _categoryRepository.GetByIdAsync(command.CategoryId);
            if (category == null)
            {
                throw new NotFoundException("Category not found");
            }

            brand.SetName(command.Name);
            brand.SetTitle(command.Title);
            brand.SaveChanges();

            _brandRepository.Update(brand);
            await _unitOfWork.CommitAsync(ct);

            return _mapper.Map<UpdateBrandDto>(brand);
        }
    }
}
```