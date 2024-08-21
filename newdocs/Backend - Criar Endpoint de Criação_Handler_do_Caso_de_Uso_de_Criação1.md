```csharp
namespace Project.Application.UseCases.Brands.CreateBrand
{
    public class CreateBrandHandler : ICommandHandler<CreateBrandCommand, CreateBrandDto>
    {
        private readonly IBrandFactory _brandFactory;
        private readonly IBrandRepository _brandRepository;
        private readonly IOrganizationRepository _organizationRepository;
        private readonly ICategoryRepository _categoryRepository;
        private readonly IUnitOfWork _unitOfWork;
        private readonly IMapper _mapper;

        public CreateBrandHandler(
            IBrandFactory brandFactory,
            IBrandRepository brandRepository,
            IOrganizationRepository organizationRepository,
            ICategoryRepository categoryRepository,
            IUnitOfWork unitOfWork,
            IMapper mapper)
        {
            _brandFactory = brandFactory;
            _brandRepository = brandRepository;
            _organizationRepository = organizationRepository;
            _categoryRepository = categoryRepository;
            _unitOfWork = unitOfWork;
            _mapper = mapper;
        }

        public async Task<CreateBrandDto> Handle(CreateBrandCommand command, CancellationToken ct = default)
        {
            var organization = await _organizationRepository.GetByIdAsync(command.OrganizationId);
            if (organization is null)
            {
                throw new NotFoundException("Organization not found");
            }

            var category = await _categoryRepository.GetByIdAsync(command.CategoryId);
            if (category is null)
            {
                throw new NotFoundException("Category not found");
            }

            var brand = _brandFactory.Create(command.Id, organization, category, command.Name, command.Title);

            await _brandRepository.CreateAsync(brand);
            
            await _unitOfWork.CommitAsync(ct);

            return _mapper.Map<CreateBrandDto>(brand);
        }
    }
}
```